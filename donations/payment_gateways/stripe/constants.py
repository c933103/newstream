from site_settings.models import GATEWAY_CAN_EDIT_SUBSCRIPTION, GATEWAY_CAN_TOGGLE_SUBSCRIPTION, GATEWAY_CAN_CANCEL_SUBSCRIPTION

API_CAPABILITIES = [GATEWAY_CAN_EDIT_SUBSCRIPTION, GATEWAY_CAN_TOGGLE_SUBSCRIPTION, GATEWAY_CAN_CANCEL_SUBSCRIPTION]
EVENT_CHECKOUT_SESSION_COMPLETED = 'checkout.session.completed'
EVENT_INVOICE_CREATED = 'invoice.created'
EVENT_INVOICE_PAID = 'invoice.paid'
EVENT_CUSTOMER_SUBSCRIPTION_UPDATED = 'customer.subscription.updated'
EVENT_CUSTOMER_SUBSCRIPTION_DELETED = 'customer.subscription.deleted'