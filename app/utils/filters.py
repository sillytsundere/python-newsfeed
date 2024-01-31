# will write jinja filters as regular Python functions here

def format_date(date):
    return date.strftime('%m/%d/%y')
# format_date function expects to receive a datetime object and use the strftime method to convert it to a string
# '%m/%d/%y' format code results in the month/day/year date format

def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]
# this code leaves only the domain name, removing unecessary info
# replace() and split() methods behave the same as they do in JS

def format_plural(amount, word):
    if amount != 1:
      return word + 's'
    
    return word