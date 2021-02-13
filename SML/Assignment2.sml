(*1*)
fun isPrime(n)=
let 
   fun Divisors(k,i)=
    if i*i<=(k) then
    if k mod i=0 then false
    else Divisors(k,i+1)
  else true;
in
   if n=0 then false
   else if n=2 then true
   else
     if Divisors(n,2) then true
     else false
end;

fun check1(i,j,n)=
    if isPrime(i) andalso i+j+2<=n then
      if isPrime(j) andalso isPrime(n-i-j) then j
      else check1(i,j+1,n)
    else 0;
fun check(i,n)=
if i+4<=n then
    if check1(i,2,n)>0 then (i,check1(i,2,n),n-i-check1(i,2,n))
    else check(i+1,n)
  else (0,0,0);

fun findPrimes(n)=
 check(2,n);
findPrimes(1073500182);



(*2*)
fun max(a,b)=
  if a>b then a
  else b;

fun maximumValue(n,v,w,W)=
  if n=0 orelse W=0 then 0
  else if w(n)>W then maximumValue(n-1,v,w,W)
  else max(maximumValue(n-1,v,w,W),v(n)+maximumValue(n-1,v,w,W-w(n)));

fun v(n)=
if n=1 then 500
else if n=2 then 700
else if n=3 then 300
else if n=4 then 200
else if n=5 then 300
else 0;

fun w(n)=
if n=1 then 40
else if n=2 then 80
else if n=3 then 30
else if n=4 then 50
else if n=5 then 20
else 0;
maximumValue(5,v,w,120);



(*3.1*)
fun intToString(n)=
let
  val d=n mod 10;
in
  if n<>0 then
   if d=0 then intToString(n div 10)^"0"
   else if d=1 then intToString(n div 10)^"1"
   else if d=2 then intToString(n div 10)^"2"
   else if d=3 then intToString(n div 10)^"3"
   else if d=4 then intToString(n div 10)^"4"
   else if d=5 then intToString(n div 10)^"5"
   else if d=6 then intToString(n div 10)^"6"
   else if d=7 then intToString(n div 10)^"7"
   else if d=8 then intToString(n div 10)^"8"
   else if d=9 then intToString(n div 10)^"9"
   else raise Fail("Not Valid")
 else ""
end;

fun factor(x)= if x=0 then 60
else if x=1 then 60
else if x=2 then 24
else if x=3 then 365
else 1000;

fun name(x)= if x=0 then "seconds"
else if x=1 then "minutes"
else if x=2 then "hours"
else if x=3 then "days"
else "years";


fun productRec(k,factor)=
if k=0 then factor(0)
else productRec(k-1,factor)*factor(k);

fun findkRec(n,factor,k)=
if n<factor(k) then k
else findkRec(n div factor(k),factor,k+1);

fun termRec(n,factor,k)=
if k=0 then n mod factor(0)
else (n div productRec(k-1, factor)) mod (factor(k));

fun mergingRec(n,name,factor,k)=
if k=findkRec(n,factor,1) then ""
else 
 if termRec(n,factor,k)=0 then mergingRec(n,name,factor,k+1)
 else mergingRec(n,name,factor,k+1)^" "^intToString(termRec(n,factor,k))^name(k);

fun convertUnitsRec(n,name,factor)=
mergingRec(n,name,factor,0);

convertUnitsRec(1073741823,name,factor);


(*3.2*)
fun productIter(k,factor,product)=
if k=0 then product*factor(0)
else productIter(k-1,factor,product*factor(k));

fun findkIter(n,factor,k)=
if n<factor(k) then k
else findkIter(n div factor(k),factor,k+1);

fun termIter(n,factor,k)=
if k=0 then n mod factor(0)
else (n div productIter(k-1, factor,1)) mod (factor(k));

fun mergingIter(n,name,factor,k,result)=
  if k=findkIter(n,factor,1) then result
  else if termIter(n,factor,k)=0 then                                                    mergingIter(n,name,factor,k+1,result)
  else mergingIter(n,name,factor,k+1,"  "^intToString(termIter(n,factor,k))^name(k)^result);

fun convertUnitsIter(n,name,factor)=
  mergingIter(n,name,factor,0,"");

convertUnitsIter(1073741823,name,factor);



(*4*)
fun powerIter(n,i,power1,c)=
if c=i then power1
else powerIter(n,i,power1*n,c+1);

fun findP(n,k)=
if n div powerIter(4,k,1,0)<4 then k
else findP(n,k+1);

fun intSqrt1(n,a,sqrt,c,d)=
if c<a+1 then
  if (2*sqrt+1)*(2*sqrt+1)>n div d  then intSqrt1(n,a,2*sqrt,c+1,d div 4)
  else  intSqrt1(n,a,2*sqrt+1,c+1,d div 4)
else sqrt;

fun intSqrt(n)=
intSqrt1(n,findP(n,0),0,0,powerIter(4,findP(n,0),1,0));

intSqrt(400000000);
