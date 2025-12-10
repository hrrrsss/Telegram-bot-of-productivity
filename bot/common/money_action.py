from yoomoney import Quickpay, Client

from config.config import settings


def create_paid_link(tg_id: int):
    receiver = settings.receiver

    label = f"pay_num{str(tg_id)}"

    quickpay = Quickpay(
              receiver=receiver,
              quickpay_form="shop",
              targets="Оплата платного PDF",
              paymentType="AC",
              label=label,
              sum=4
       )
    
    return quickpay.redirected_url


def check_paid(tg_id: int):
    token = settings.acces_token
    label = f"pay_num{str(tg_id)}"

    client = Client(token)
    history = client.operation_history()

    operation = {op.label: op.status for op in history.operations}

    print(operation)

    if label in operation:
        if operation[label] == "success":
            return True
    return False