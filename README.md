# Odoo NumVerify
NumVerify offers a full-featured yet simple RESTful JSON API for national and international phone number validation and information lookup for a total of 232 countries around the world. In this project, NumVerify will integrate with Odoo to make sure that the Phone Number and the Country are matching.

This module can validate the phone and mobile in the customers form too [res.partner].

#### How it works:
All you need is to [NumVerify](https://numverify.com/documentation) website and register for free to get your API Access Key.
In Odoo, Navigate to `Website > Configuration > Settings`, check "Enable VerifyNum" and add API Access Key.

When a customer add his own details in the checkout form it will check if the Phone Number and the country are matching. If not, an error will be raised with a description about what went wrong so that the customer can fix it before proceeding with the checkout process.
