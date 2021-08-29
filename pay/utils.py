import random
import string
from django.conf import settings
from django.core.cache import cache

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def unique_card_id_generator(instance):
	card_new_id= random_string_generator()

	Klass= instance.__class__

	qs_exists= Klass.objects.filter(card_id= card_new_id).exists()
	if qs_exists:
		return unique_card_id_generator(instance)
	return card_new_id
