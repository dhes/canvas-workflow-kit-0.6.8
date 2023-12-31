import arrow


class Timeframe(object):

    def __init__(self, start: arrow.Arrow, end: arrow.Arrow):
        self.start = start
        self.end = end

    def __str__(self):
        return f'<Timeframe start={self.start}, end={self.end}>'

    # the duration of the time frame defines the duration
    @property
    def duration(self) -> int:
        return (self.end - self.start).days

    def increased_by(self, years: int = 0, months: int = 0, days: int = 0):
        start = self.start
        end = self.end

        if years > 0:
            end = end.shift(years=years)
        elif years < 0:
            start = start.shift(years=years)

        if months > 0:
            end = end.shift(months=months)
        elif months < 0:
            start = start.shift(months=months)

        if days > 0:
            end = end.shift(days=days)
        elif days < 0:
            start = start.shift(days=days)

        return Timeframe(start=start, end=end)
