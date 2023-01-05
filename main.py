from api.api import TimeTreeApi

API_ACCESS_TOKEN = "o6N5520I7U78NSuY17wWA4i7XvzSwRSWwrZiz2YqvB2sdzG_"

def main():
    client = TimeTreeApi(API_ACCESS_TOKEN)
    calendars = client.get_calendars()

    calendar_id = None

    if(len(calendars.data) > 0):
        calendar_id = calendars.data[0].id
    else:
        print("Only supporting one calendar at a time, but found "+str(len(calendars)))
        return

    calendar = client.get_calendar(calendar_id=calendar_id)
    events = client.get_upcoming_events(calendar_id=calendar_id)

    print(str(events.data))

if __name__ == "__main__":
    main()