# -*- coding: utf-8 -*-

# Copyright (C) 2009 - 2010 Ulteo SAS
# http://www.ulteo.com
# Author Julien LANGLOIS <julien@ulteo.com> 2009, 2010
#
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 2
# of the License
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Platform = None

if Platform is None:
	from ovd import util
	p = util.get_platform()
	
	if p == "linux":
		from Linux.System import System
	
	elif p == "windows":
		from Windows.System import System
		
	else:
		raise Exception("Not supported platform")
		
	class _Platform:
		pass
	Platform = _Platform()
	Platform.System = System