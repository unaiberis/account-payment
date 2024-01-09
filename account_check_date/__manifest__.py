# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Check Date",
    "version": "15.0.0.1.0",
    "author": "Ecosoft, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-payment",
    "license": "AGPL-3",
    "category": "Accounting & Finance",
    "summary": "Add check date on payment for check printing",
    "depends": [
        "account_check_printing",
        # [T5871] Fixing: ValueError: Invalid field 'invoice_is_snailmail' on
        # model 'res.config.settings' while doing configuration of account.journal
        "snailmail_account",
    ],
    "data": [
        "views/account_payment_views.xml",
        "wizard/account_payment_register_views.xml",
    ],
    "installable": True,
    "post_init_hook": "assign_check_date",
    "development_status": "Alpha",
    "maintainers": ["ps-tubtim"],
}
