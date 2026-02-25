import tkinter as tk
import json
import threading
import requests

import repair_wireless_main_integ
import ship_main_integ
import self_install_main_integ
import vacation_rest_main_integ
import vacation_susp_main_integ
import order_cancel_main_integ
import order_complete_main_integ
import conf_change_main_integ
import conf_disc_main_integ
import conf_new_main_integ
import conftf_main_integ
import Bill_firstbill_new_main_integ
import bill_first_change_main_integ
import bill_firstbill_tf_main_integ
import bill_disconnect_final_main_integ
import openpyxl
import os
import datetime
import tkinter.messagebox

TEMPLATE_TO_MODULE = {
    "ECOM.ORDERING.SHIPPINGCONF": ship_main_integ,
    "ECOM.ACCTMGMT.TECH": self_install_main_integ,
    "Ecom.Ordering.VacationRestore": vacation_rest_main_integ,
    "Ecom.Ordering.VacationSuspend": vacation_susp_main_integ,
    "ECOM.ORDERING.CANCELLED": order_cancel_main_integ,
    "ECOM.ORDERING.COMPLETE": order_complete_main_integ,
    "ECOM.ORDERING.CONFCHANGE": conf_change_main_integ,
    "ECOM.ORDERING.CONFDISCONNECT": conf_disc_main_integ,
    "ECOM.ORDERING.CONFNEW": conf_new_main_integ,
    "ECOM.ORDERING.CONFTF": conftf_main_integ,
    "ECOM.BILLING.FIRSTBILLNEW": Bill_firstbill_new_main_integ,
    "ECOM.BILLING.FIRSTBILLCHANGE": bill_first_change_main_integ,
    "ECOM.BILLING.FIRSTBILLTF": bill_firstbill_tf_main_integ,
    "ECOM.BILLING.DISCONNECTFINALBILL": bill_disconnect_final_main_integ,
    "ECOM.REPAIR.WIRELESSCREDS" : repair_wireless_main_integ
}

WORKFLOW_URL = "https://ntfwf-notification-service-test1.rke-odc-test.corp.intranet/api/notification/workflow"



testcase_results = []

def extract_template(payload):
    for attr in payload.get("dataAttributes", []):
        if attr.get("name") == "TEMPLATE":
            return attr.get("value")
    return None

def run_testcases():
    global testcase_results
    try:
        progress_var.set("Running test cases...")
        run_button.config(state=tk.DISABLED)
        payload = json.loads(text_input.get("1.0", tk.END))
        template = extract_template(payload)
        if not template:
            update_result("TEMPLATE not found in payload.")
            return
        module = TEMPLATE_TO_MODULE.get(template)
        if not module or not hasattr(module, "generate_testcases"):
            update_result(f"No test case generator for template: {template}")
            return
        testcases = module.generate_testcases(payload)
        results = []
        headers = {"Content-Type": "application/json"}
        testcase_results = []
        for idx, tc in enumerate(testcases, 1):
            description = tc.get("description", "No description provided")
            progress_var.set(f"Running test case {idx}/{len(testcases)}...")
            try:
                resp = requests.post(WORKFLOW_URL, headers=headers, data=json.dumps(tc), timeout=10, verify=False)
                status = resp.status_code
                reason = resp.reason
                headers_str = json.dumps(dict(resp.headers), indent=2)
                resp_text = resp.text
                if status >= 400:
                    status_str = f"ERROR ({status} {reason})"
                else:
                    status_str = f"SUCCESS ({status} {reason})"
            except Exception as e:
                resp_text = str(e)
                status_str = "EXCEPTION"
                headers_str = ""
            results.append(
                f"Test Case {idx}:\nDescription: {description}\nRequest:\n{json.dumps(tc, indent=2)}\n\n"
                f"Response ({status_str}):\nHeaders:\n{headers_str}\n\nBody:\n{resp_text}\n{'='*60}\n"
            )
            testcase_results.append((idx, description, tc, status_str, resp_text))
            update_result("\n".join(results))
        progress_var.set("Done.")
    except Exception as e:
        update_result(f"Error: {e}")
        progress_var.set("Error.")
    finally:
        run_button.config(state=tk.NORMAL)

def save_results_to_excel():
    if not testcase_results:
        tk.messagebox.showwarning("No Results", "No test results to store. Run tests first.")
        return
    # Extract template from the last test case's payload
    last_payload = testcase_results[-1][2]
    template = extract_template(last_payload)
    if not template:
        template = "unknown_template"
    template = template.replace(".", "_")
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    save_dir = os.path.expanduser("~/Documents/ApiTestResults")
    os.makedirs(save_dir, exist_ok=True)
    filename = f"{template}_api_test_results_{now}.xlsx"
    filepath = os.path.join(save_dir, filename)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Results"
    ws.append(["Test Case", "Description", "Request", "Status", "Response"])
    for idx, description, payload, status, resp_text in testcase_results:
        ws.append([
            f"Test Case {idx}",
            description,
            json.dumps(payload, indent=2),
            status,
            resp_text
        ])
    wb.save(filepath)
    tk.messagebox.showinfo("Saved", f"Results stored in {filepath}")

def update_result(text):
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, text)
    result_text.config(state=tk.DISABLED)

def on_submit():
    threading.Thread(target=run_testcases).start()

root = tk.Tk()
root.title("Workflow Test Runner")

tk.Label(root, text="Paste Payload JSON:").pack()
text_input = tk.Text(root, height=12, width=80)
text_input.pack()

run_button = tk.Button(root, text="Run Testcases", command=on_submit)
run_button.pack()

save_button = tk.Button(root, text="Save Results to Excel", command=save_results_to_excel)
save_button.pack()

progress_var = tk.StringVar()
tk.Label(root, textvariable=progress_var).pack()

result_frame = tk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = tk.Text(result_frame, height=20, width=80, wrap=tk.NONE, yscrollcommand=scrollbar.set, state=tk.DISABLED)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=result_text.yview)

root.mainloop()

