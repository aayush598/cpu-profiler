https://learn.arm.com/install-guides/perf/

Thanks for the detailed log — this is a **very common issue** on newer Ubuntu/Linux systems. You're getting the error because the system is **blocking access to low-level CPU performance events** for unprivileged users.

Let’s fix this. 👇

---

## 🔧 Fix: `perf_event_paranoid` is Too Restrictive

Your system currently has:

```
perf_event_paranoid = 4
```

This **blocks all perf usage**, even basic events like `cycles` and `instructions`.

---

### ✅ **Option 1: Temporary Fix (Just for Now)**

Set it to a more permissive level **for this session**:

```bash
sudo sysctl -w kernel.perf_event_paranoid=1
```

Or even:

```bash
sudo sysctl -w kernel.perf_event_paranoid=0
```

Now try running your Python script again:

```bash
python main.py
```

✅ It should now work and show `cycles`, `instructions`, etc.

---

### 🔁 **Option 2: Permanent Fix (Survives Reboot)**

If the temporary fix works, make it permanent:

1. Open the sysctl config:

```bash
sudo nano /etc/sysctl.conf
```

2. Add this line to the bottom:

```bash
kernel.perf_event_paranoid = 1
```

3. Save and apply it:

```bash
sudo sysctl -p
```

---

### ⚠️ Notes on Security and Levels

| Value | Meaning                                                         |
| ----- | --------------------------------------------------------------- |
| `-1`  | Full access (most permissive) — allows raw kernel event tracing |
| `0`   | Allow CPU events + kernel profiling                             |
| `1`   | Allow CPU events, **disallow kernel profiling**                 |
| `2`   | Disallow CPU events for unprivileged users                      |
| `3+`  | Completely disable perf use without root                        |

💡 **Recommended for development**: use `kernel.perf_event_paranoid = 1`

---

### 🧪 After the Fix

Re-run your script:

```bash
python main.py
```

Expected output:

```
[ PERF STATS ]
 Performance counter stats for 'python3 -c ...':
    512,385,000 cycles
    507,123,000 instructions
         93,456 cache-misses
   0.612321 seconds time elapsed
```

---

### ✅ Next Step

Once you confirm `perf` is working, we can:

* Parse the output into structured data
* Combine timing + psutil + perf into one clean report
* Or move on to Phase 4: JSON Logging

Would you like help parsing `perf` output into a dictionary next?




python main.py --file example.py --output reports/my_custom_report.json