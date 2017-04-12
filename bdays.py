from datetime import datetime, timedelta

class Person():
	"""
	Defines a person by his birthday
	methods:
	age
	age difference from another person
	"""
	
	def __init__(self, year=1992, month=9, day=17):
		self.bday=datetime(year, month, day)
		
		
	def birthday(self):
		"""prints the birthday as a string"""
		return datetime.strftime(self.bday, '%a %d %b %Y')
	

	def days_to_years(self, days):
		"""returns a tuple (years, months, days) equilvalent to the given number of days"""
		years, days= divmod(days,365.2524)
		months,days= divmod(days,30)
		return (years, months, days)
	
	
	def seconds_to_hours(self, seconds):
		"""returns a tuple (hh,mm,ss) equivalent to the number of seconds given"""
		hours,seconds= divmod(seconds, 3600)
		minutes, seconds= divmod(seconds, 60)
		return (hours, minutes, seconds)
	
	
	def age(self):
		"""return the age of the person in years (float)"""
		born= self.bday
		now= datetime.today()
		return now.year - born.year - (born.month > now.month)
		
		
	def age_in(self, date):
		"""returns the person's age for a given date tuple(y,m,d,h,m,s)"""
		assert isinstance(date, datetime) and (date>self.bday)
		delta= date-self.bday
		#calculate years, months and days
		years, months, days = self.days_to_years(delta.days)
		hours, minutes, seconds = self.seconds_to_hours(delta.seconds)
		return (years, months, days, hours, minutes, seconds)
        
        
	def time_to_birthday(self):
		"""returns months, days till next birthday tuple(m,d,h,m,s)"""
		bday=self.bday
		today=datetime.today()
		tmp= datetime(today.year, bday.month, bday.day)
		nxt_bday= datetime(today.year+ (today>tmp), bday.month, bday.day)
		delta=nxt_bday-today
		return self.days_to_years(delta.days)+self.seconds_to_hours(delta.seconds)
		
		
	def age_diff(self, dude):
		"""returns the age difference between the given person"""
		assert( isinstance(dude, Person))
		return abs(self.age() - dude.age())
		
		
	def time_to_age(self, age):
		"""returns time left to reach a given age"""
		assert age>self.age()
		bday=self.bday
		today=datetime.today()
		nxt= datetime(today.year+age-self.age(), bday.month, bday.day)
		delta= nxt-today
		return self.days_to_years(delta.days)+self.seconds_to_hours(delta.seconds)
	
	
	def double_year(self, dude):
		"""returns the number of years left to reach double year.
		For two people born on different days, there is a day when one is twice as old as the
		other. That’s their Double Day."""
		assert( isinstance(dude, Person) and dude.bday!=self.bday)
		a,b= max(self.age(), dude.age()), min(self.age(), dude.age())
		if a==b:
			return 'Both are born on the same year!'
		elif a>=2*b:
			return a-2*b
		else:
			return 'The double year was {} years ago'.format(a-2*b)

''' test case'''
	
joe=Person(2010, 2, 19)	#7 yo
pete=Person(2000, 2,19)	#17 yo

print('Joe, bday, age, age_diff_pete, time_to_bday \n',
joe.bday,
joe.age(),
joe.age_diff(pete),
joe.time_to_birthday(),
'\n\nPete, bday, age, age_diff_joe, time_to_age(20), age_in(2020,2,19) \n',
pete.bday,
pete.age(),
pete.age_diff(joe),
pete.time_to_age(20),
pete.age_in(datetime(2020,2,19)),
pete.double_year(joe),

)
