
from odoo import api, models, _
from odoo.exceptions import ValidationError, UserError
from odoo.http import request
import logging


_logger = logging.getLogger(__name__)

try:
    from stdnum.do import ncf as ncf_validation

except (ImportError, IOError) as err:
    _logger.debug(err)
 
    
class AccountMove(models.Model):
    _inherit = "account.move"  

    @api.onchange("l10n_latam_document_number", "l10n_do_origin_ncf")
    def _onchange_l10n_latam_document_number(self):
        dgii_autocomplete = request.env['ir.config_parameter'].sudo(
        ).get_param('l10n_do_rnc_search.dgii_autocomplete')

        for rec in self.filtered(
            lambda r: r.company_id.country_id == self.env.ref("base.do")
            and r.l10n_latam_document_type_id.l10n_do_ncf_type is not False
            and r.journal_id.l10n_latam_use_documents
            and r.l10n_latam_document_number
            and r.type == "in_invoice"
        ):

            NCF = rec.l10n_latam_document_number if rec.l10n_latam_document_number else None
            if not ncf_validation.is_valid(NCF):
                raise UserError(_(
                    "NCF mal digitado\n\n"
                    "El comprobante *{}* no tiene la estructura correcta "
                    "valide si lo ha digitado correctamente")
                    .format(NCF))

            if NCF[-10:-8] == '02' or NCF[1:3] == '32':
                raise ValidationError(_(
                    "NCF *{}* NO corresponde con el tipo de documento\n\n"
                    "No puede registrar Comprobantes Consumidor Final (02)")
                    .format(NCF))

            if dgii_autocomplete == 'True':
                if (
                    not ncf_validation.check_dgii(self.partner_id.vat, NCF)
                    and ncf_validation.is_valid(NCF)
                    and len(NCF) == 11

                ):
                    raise ValidationError(_(
                        u"NCF NO pasó validación en DGII\n\n"
                        u"¡El número de comprobante *{}* del proveedor "
                        u"*{}* no pasó la validación en "
                        "DGII! Verifique que el NCF y el RNC del "
                        u"proveedor estén correctamente "
                        u"digitados, o si los números de ese NCF se "
                        "le agotaron al proveedor")
                        .format(NCF, self.partner_id.name))