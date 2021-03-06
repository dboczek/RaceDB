from django.core.management.base import BaseCommand, CommandError
from core.models import *
import core.init_ccn

class Command(BaseCommand):

	args = '<ccn_sheet.xls>'
	help = 'Initialize the database with CCN data'

	def handle(self, *args, **options):
		core.init_ccn.init_ccn( *args )
