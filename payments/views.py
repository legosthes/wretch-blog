from django.shortcuts import render
import braintree


def new(request):
    plan = request.GET.get("plan")
    # 擋非預期方案，防呆
    avaiable_plans = ["a", "b", "c"]
    if plan.lower() not in avaiable_plans:
        # 我直接幫你挑方案，而不是完全擋掉
        plan = "a"

    # token
    # key 不要上傳上去
    gateway = braintree.BraintreeGateway(
        braintree.Configuration(
            environment=braintree.Environment.Sandbox,
            merchant_id="",
            public_key="",
            private_key="",
        )
    )
    token = gateway.client_token.generate()

    return render(
        request,
        "payments/new.html",
        {
            "plan": plan,
            "token": token,
        },
    )


def index(request):
    pass
