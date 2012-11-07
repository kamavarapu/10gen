<!DOCTYPE html>
<html>
<head>
<title>{{title}}</title>
</head>
<body>
<p>
Welcome {{username}}
<p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
</body>
</html>