from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from shop.models import *
from datetime import datetime, timedelta
@periodic_task(run_every=crontab(minute='*/4'))
def send_report():
	subject = "Sales Report - Bitgray Store"
	to = ['davidcp90@gmail.com']
	from_email = 'report@bitgraystore.com'
	earns=0
	purchases=Compras.objects.filter(pub_date__gte=datetime.now()-timedelta(days=7))
	for l in purchases:
                    if l.id_producto:
                        if l.precio:
                            earns=earns+int(l.precio)
                        else:
                            pr=Productos.objects.get(id=l.id_producto)
                            earns=earns+int(pr.precio)
	data = {
		'max_diff': max_diff
		'avg_diff': avg_diff
		'min_diff': min_diff
		'purchases': purchases.count()
		'earns': earns
		'ppm': purchases.count()/(7*24*60)
	}
	message = render_to_string('report.html', data)
	EmailMessage(subject, message, to=to, from_email=from_email).send()