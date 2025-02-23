class AllreadyBookedEvent(Exception):
    """Already booked event """
    
class EmptySeats(Exception):
    """ no availble seats """
    
class DateError(Exception):
    """❌  wrong date format. Use (YYYY-M-D) """