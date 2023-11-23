# README

## Finance Calendar Notifier

This Python script provides a daily finance calendar report, including earnings, dividends, IPOs, splits, and dividend history. The script utilizes the `finance_calendars` library to fetch data and sends the results via Telegram for easy monitoring.

### Dependencies

Make sure you have the following Python libraries installed:

- finance_calendars
- pandas
- telegram-send

You can install them using:

```bash
pip install finance_calendars pandas telegram-send
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/repo.git
cd repo
```

2. Run the script:

```bash
python finance_calendar_notifier.py
```

### Configuration

Adjust the following parameters in the script to customize your notifications:

- `G_WAIT`: The waiting time (in seconds) between Telegram messages.
- `G_tomorrowFlag` and `G_todayflag`: Set to `True` if you want to receive notifications for tomorrow's and today's events, respectively.

### Results

The script fetches and sends notifications for the following finance calendar events:

- **Earnings**: Today and tomorrow's earnings announcements.
- **Dividends**: Today and tomorrow's dividend ex-dates and payment dates.
- **IPOs**: Priced, filed, withdrawn, and upcoming IPOs for the current month.
- **Splits**: Today's and specified date splits.
- **Dividend History**: Historical dividends for specified stocks and ETFs.

### Disclaimer

This script is for informational purposes only. It is not financial advice, and the developer is not responsible for any trading decisions made based on its results.

Feel free to contribute to and enhance the script. Stay informed and happy investing!
