from django.shortcuts import render, redirect
import braintree
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dotenv import load_dotenv
import os

load_dotenv()


PRICE_LIST = {
    "a": 10,
    "b": 50,
    "c": 100,
}



@login_required
def new(request):
    plan = request.GET.get("plan")
    # 擋非預期方案，防呆
    avaiable_plans = ["a", "b", "c"]
    if plan.lower() not in avaiable_plans:
        # 我直接幫你挑方案，而不是完全擋掉
        plan = "a"

    # token
    token = gateway().client_token.generate()

    return render(
        request,
        "payments/new.html",
        {"plan": plan, "token": token, "price": PRICE_LIST.get(plan)},
    )


@login_required
@require_POST
def index(request):
    nonce = request.POST.get("nonce")
    plan = request.POST.get("plan")

    result = gateway().transaction.sale(
        {
            "amount": PRICE_LIST.get(plan),
            "payment_method_nonce": nonce,
        }
    )

    if result.is_success:
        messages.success(request, "Purchase successful.")
    else:
        messages.error(request, "Purchase failed, please try again.")

    return redirect("articles:index")


def gateway():
    # key 不要上傳上去
    return braintree.BraintreeGateway(
        braintree.Configuration(
            environment=braintree.Environment.Sandbox,
            # 這裡就是用env檔案帶進來，不會hard code在這裡，也比較安全
            merchant_id=os.getenv("merchant_id"),
            public_key=os.getenv("public_key"),
            private_key=os.getenv("private_key"),
        )
    )
