# This contains some helper methods based for lists
# Copyright (C) 2012  Gaurav Agrawal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def union(listA, listB) : 
	for i in listB : 
		if i not in listA : 
			listA.append(i)

def get_non_intersecting(listA, listB) :
	result = []
	for l in listA : 
		if l not in listB : 
			result.append(l)

	return result

def printList(list) : 
	for l in list : 
		print l