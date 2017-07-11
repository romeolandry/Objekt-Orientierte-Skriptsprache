from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

secretKey = settings.STRIPE_SCRET_KEY

# Create your views here.

@login_required
def checkout(request):
    publiskey = settings.STRIPE_PUBLISHABLE_KEY
    context={}
    if request.method == 'GET':
        print('in the get methode')
        amount=8000;
        context = {'publiskey': publiskey, 'charge': amount}
        template = 'checkout.html'
        return render(request, template, context)

    if request.method=='POST':
        token = request.POST['stripeToken']
        print ('le post')
        print (token)
        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency="euro",
                source=token,
                description="Example of charge"
            )
            context = {'publiskey': publiskey, 'charge': charge}
        except stripe.error.CardError as e:
            pass
    template='checkout.html'
    return render(request, template,context)
