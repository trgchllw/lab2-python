def check_events_simple(events):

    sorted_events = sorted(events, key=lambda x: x["start"])

    for i in range(len(sorted_events)):
        for j in range(i + 1, len(sorted_events)):
            event1 = sorted_events[i]
            event2 = sorted_events[j]

            if event1["start"] >= event1["end"] or event2["start"] >= event2["end"]:
                continue

            if event2["start"] < event1["end"]:
                print(f"Конфликт: {event1['title']} ({event1['start']}–{event1['end']}) "
                      f"и {event2['title']} ({event2['start']}–{event2['end']})")


events = [
    {"title": "Math", "start": "09:00", "end": "10:30"},
    {"title": "English", "start": "10:00", "end": "11:00"}
]

check_events_simple(events)