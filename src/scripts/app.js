//原始檔在這裡，透過打包再送去public/scripts
//打包後的東西，用不到的東西，會幫你丟掉
import Alpine from "alpinejs";
import "htmx.org";
import { BrainTreePayment } from "./braintree";

window.Alpine = Alpine;

Alpine.data("braintree_payment_form", BrainTreePayment);

Alpine.start();
