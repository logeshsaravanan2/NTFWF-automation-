import importlib
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import openpyxl
import datetime

template_to_module = {
    "ECOM.ORDERING.SHIPPINGCONF": "ship_conf_new",
    "ECOM.ACCTMGMT.TECH": "self_install_new",
    "Ecom.Ordering.VacationRestore": "vacation_restore_new",
    "Ecom.Ordering.VacationSuspend": "vacation_suspend_new",
    "ECOM.REPAIR.WIRELESSCREDS" : "repair_wireless",
    "ECOM.ACCTMGMT.VMRESET" : "repair_VM_reset"

}

class BaseTestRunnerUI:
    def __init__(self, master, template_to_module):
        self.master = master
        self.template_to_module = template_to_module
        self.template_names = list(template_to_module.keys())
        self.selected_template = tk.StringVar(value=self.template_names[0])
        self.responses = []
        master.title("API Test Runner")
        tk.Label(master, text="Select Template:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        ttk.Combobox(master, textvariable=self.selected_template, values=self.template_names, state="readonly", width=60).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        tk.Button(master, text="Test", command=self.run_tests, width=20).grid(row=1, column=1, padx=10, pady=5, sticky='e')
        self.response_text = scrolledtext.ScrolledText(master, width=100, height=30)
        self.response_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(master, text="Store Results in Excel", command=self.store_results, width=30).grid(row=3, column=0, columnspan=2, pady=10)

    def run_tests(self):
        import requests, json
        template = self.selected_template.get()
        module_name = self.template_to_module[template]
        mod = importlib.import_module(module_name)
        testcases = getattr(mod, "testcases")
        testcase_descriptions = getattr(mod, "testcase_descriptions")
# Add this mapping at the top of your file
        template_to_url = {
            "ECOM.REPAIR.WIRELESSCREDS": "https://ntfwf-repair-test1.rke-odc-test.corp.intranet/api/notification/repair/wireless",
            "ECOM.ACCTMGMT.VMRESET": "https://ntfwf-repair-test1.gke-cm-wklds-nonprod-ue4.gcl.corp.intranet/api/notification/repair/vmreset"

        }
        default_url = "https://ntfwf-ordering-service-test1.rke-odc-test.corp.intranet/api/notification/order/config"

        # In run_tests, replace the url assignment with:
        template = self.selected_template.get()
        url = template_to_url.get(template, default_url)

        self.response_text.delete(1.0, tk.END)
        self.responses = []
        for idx, payload in enumerate(testcases, 1):
            error_message = ""
            try:
                resp = requests.post(url, json=payload, timeout=15, verify=False)
                actual = resp.json()
                if resp.status_code >= 400:
                    error_message = f"HTTP {resp.status_code}: {resp.reason}"
            except Exception as e:
                actual = str(e)
                error_message = str(e)
            self.responses.append((idx, payload, actual, error_message))
            self.response_text.insert(tk.END, f"Test Case {idx}:\nRequest:\n{json.dumps(payload, indent=4)}\nResponse:\n{json.dumps(actual, indent=4) if isinstance(actual, dict) else actual}\n")
            if error_message:
                self.response_text.insert(tk.END, f"Error: {error_message}\n")
            self.response_text.insert(tk.END, "-"*80 + "\n")
        messagebox.showinfo("Done", f"Tested {len(testcases)} cases for template '{template}'.")

    def store_results(self):
        import json
        if not self.responses:
            messagebox.showwarning("No Results", "No test results to store. Run tests first.")
            return
        template = self.selected_template.get().replace(".", "_")
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{template}_api_test_results_{now}.xlsx"
        save_dir = "/Users/ad22338/Downloads/ApiTestResults"
        os.makedirs(save_dir, exist_ok=True)
        filepath = os.path.join(save_dir, filename)
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Results"
        ws.append(["Test Case", "Request", "Response", "Error"])
        for idx, payload, actual, error_message in self.responses:
            ws.append([
                f"Test Case {idx}",
                json.dumps(payload, indent=2),
                json.dumps(actual, indent=2) if isinstance(actual, dict) else str(actual),
                error_message
            ])
        wb.save(filepath)
        messagebox.showinfo("Saved", f"Results stored in {filepath}")



if __name__ == "__main__":
    root = tk.Tk()
    app = BaseTestRunnerUI(root, template_to_module)
    root.mainloop()
