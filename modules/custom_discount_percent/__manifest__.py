# -*- coding: utf-8 -*-
{
    "name": "Product Discount Percentage on Website",
    "version": "1.0",
    "category": "Website",
    "summary": "Displays percentage discount for discounted products in eCommerce",
    "depends": ["website_sale"],
    "data": ["views/templates.xml"],
    "assets": {
        "web.assets_frontend": [
            "/custom_discount_percent/static/src/css/discount.css",
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
