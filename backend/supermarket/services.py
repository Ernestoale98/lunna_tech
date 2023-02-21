from django.core.mail import send_mail
from django.template.loader import get_template

from backend.supermarket.models import Product, ProductRequestLog
from django.conf import settings
from backend.authentication.models import User


def notify_product_was_updated(product: Product, old_product: Product, who_made_change: User) -> None:
    """Notify to all admins about product change and who did it"""
    message = get_template('product_was_update.html').render({
        'product': product,
        'old_product': old_product,
        'who_made_change': who_made_change
    })

    send_mail(
        f"{product.name} was updated by {who_made_change.email}",
        message,
        settings.EMAIL_FROM_ADDRESS,
        [user.email for user in User.objects.filter(is_superuser=True).only('email')],
        fail_silently=False,
        html_message=message
    )


def create_product_request_log(product: Product) -> ProductRequestLog:
    """Create new ProductRequestLog"""
    return ProductRequestLog.objects.create(product=product)
