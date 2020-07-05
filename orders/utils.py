import random
import string


def generate_random_string(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id(instance):
    order_id_new = generate_random_string()
    klass = instance.__class__
    qs_exist = klass.objects.filter(order_id=order_id_new).exists()
    if qs_exist:
        return unique_order_id(instance)
    return order_id_new
