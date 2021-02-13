(*1*)
fun climbStair(n)=
 if n=1 then 1
 else if n=2 then 2
 else  if n>2 then climbStair(n-1)+climbStair(n-2)
 else raise Fail("number of stairs should be greater than 0");



(*2*)
fun modifiedDigitSum(n)=
 if n>=10 then  2*modifiedDigitSum(n div 10)+ (n mod 10)
 else n;

modifiedDigitSum(132);                (* Returns 12*)



(*3*)
fun square(i,j,n)=
 if i*i+j*j=n then 1
 else if i*i+j*j<n then square(i,j+1,n)
 else 0;

fun sumofsquares(i,j,n)=
 if i*i<=n then
  if square(i,0,n)=1 then 1
  else sumofsquares(i+1,0,n)
 else 0;

fun numbers(n)=
 if n >= 0 then
  if sumofsquares(0,0,n)=1 then 1+numbers(n-1)
  else numbers(n-1)
 else 0;

fun squaredCount(n)=                (*Final Function*)
 numbers(n)-1;
squaredCount(460);                  (*returns 164*)



(*4*)
fun t(n)=                           (*For terms in series*)
 if n>1 then 
   if  n mod 2=0 then 4.0/((2.0*real(n)-2.0)*(2.0*real(n)-1.0)*(2.0*real(n)))
   else ~ 4.0/((2.0*real(n)-2.0)*(2.0*real(n)-1.0)*(2.0*real(n)))
 else if n=1 then 3.0
 else raise Fail("n should be greater than 1");

fun Sumupton(q,x)=        
 if abs(t(q))<=x then t(q) 
 else Sumupton(q+1,x)+t(q);

fun nilakanthaSum(n)=              (*Final Function*)
 Sumupton(1,n);

nilakanthaSum(0.0000085);          (*Returns3.141596556793832*)


