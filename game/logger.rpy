init -2 python:
    import time
    import csv
    import os

    log_rows = []
    _choice_shown_ts = None

    def _now():
        return time.time()

    def log_event(event_type, **fields):
        row = {
            "ts_unix": _now(),
            "event": event_type,
            "participant_id": participant_id
        }
        row.update(fields)
        log_rows.append(row)

    def log_choice_shown(choice_id):
        global _choice_shown_ts
        _choice_shown_ts = _now()
        log_event("choice_shown", choice_id=choice_id)

    def log_choice_clicked(choice_id, option_text):
        global _choice_shown_ts
        clicked_ts = _now()
        rt = clicked_ts - _choice_shown_ts if _choice_shown_ts else None
        log_event(
            "choice_clicked",
            choice_id=choice_id,
            option=option_text,
            rt_seconds=rt
        )
        _choice_shown_ts = None

    def export_log_csv(filename="mayhem_run.csv"):
        home = os.path.expanduser("~")
        outdir = os.path.join(home, "Desktop", "GreatFireLogs")
        os.makedirs(outdir, exist_ok=True)

        safe_id = participant_id if participant_id else "unknown"
        filename = "mayhem_run_%s_%d.csv" % (safe_id, int(time.time()))
        path = os.path.join(outdir, filename)

        keys = set()
        for r in log_rows:
            keys.update(r.keys())
        fieldnames = sorted(keys)

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in log_rows:
                writer.writerow(r)

        return path