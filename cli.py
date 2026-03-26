import argparse
import logging
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_order(args.type, args.price)

    print("\nOrder Summary:")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    if args.price:
        print(f"Price: {args.price}")

    if args.type == "MARKET":
        order = place_market_order(args.symbol, args.side, args.quantity)
    else:
        order = place_limit_order(args.symbol, args.side, args.quantity, args.price)

    print("\nResponse:")
    print(f"Order ID: {order.get('orderId')}")
    print(f"Status: {order.get('status')}")
    print(f"Executed Qty: {order.get('executedQty')}")
    print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    logging.info(f"Order placed: {order}")

    print("\n✅ Order placed successfully")

except Exception as e:
    logging.error(f"Error: {str(e)}")
    print(f"\n❌ Error: {str(e)}")