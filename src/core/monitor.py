import wmi

def get_real_monitors():
    try:
        obj_wmi = wmi.WMI(namespace="root\\wmi")
        monitors_id = obj_wmi.WmiMonitorID(Active=True)
        
        monitor_list = []
        for i, m in enumerate(monitors_id):
            model_name = "".join([chr(x) for x in m.UserFriendlyName if x != 0])
            if not model_name:
                model_name = f"Monitor {i+1}"
            monitor_list.append({"id": i, "name": model_name})
        return monitor_list
    except Exception:
        return []