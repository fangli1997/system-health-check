#!/usr/bin/env python3

import os
import platform
import shutil
import time


def get_memory():
    try:
        import psutil
        memory = psutil.virtual_memory()
        return memory.total, memory.used, memory.percent
    except ImportError:
        return None, None, None


def get_cpu_usage():
    try:
        import psutil
        return psutil.cpu_percent(interval=1)
    except ImportError:
        return None


def get_disk_usage():
    usage = shutil.disk_usage(os.path.abspath(os.sep))
    used_percent = (usage.used / usage.total) * 100
    return usage.total, usage.used, used_percent


def format_bytes(value):
    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if value < 1024:
            return f"{value:.1f} {unit}"
        value /= 1024

    return f"{value:.1f} PB"


def main():
    print("=" * 45)
    print("        SYSTEM HEALTH CHECK")
    print("=" * 45)

    print(f"OS:           {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Hostname:     {platform.node()}")
    print(f"Python:       {platform.python_version()}")

    cpu = get_cpu_usage()

    if cpu is not None:
        print(f"CPU Usage:    {cpu:.1f}%")
    else:
        print("CPU Usage:    Install psutil")

    total, used, percent = get_memory()

    if total is not None:
        print(f"Memory:       {format_bytes(used)} / {format_bytes(total)}")
        print(f"Memory Usage: {percent:.1f}%")
    else:
        print("Memory:       Install psutil")

    disk_total, disk_used, disk_percent = get_disk_usage()

    print(
        f"Disk Usage:   {format_bytes(disk_used)} / "
        f"{format_bytes(disk_total)}"
    )
    print(f"Disk Used:    {disk_percent:.1f}%")

    print("-" * 45)

    warnings = []

    if cpu is not None and cpu >= 90:
        warnings.append("High CPU usage")

    if percent is not None and percent >= 90:
        warnings.append("High memory usage")

    if disk_percent >= 90:
        warnings.append("Low disk space")

    if warnings:
        print("Status:       WARNING")
        for warning in warnings:
            print(f"  - {warning}")
    else:
        print("Status:       HEALTHY")

    print("=" * 45)


if __name__ == "__main__":
    main()
