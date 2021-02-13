(*1*)

(*1.a*)
fun LgintToInt(l)=
if length(l)>=10 then 1000000000
else if null(l) then 0
else hd(l)+10*LgintToInt(tl(l));
LgintToInt([1,2,3,9,7,3,5]);


(*1.b*)
fun intToLgint(n)=
if n=0 then [0]
else
  let fun intToList(n)=
      if n=0 then []
      else [n mod 10]@intToList(n div 10);
  in
      intToList(n)
  end;
intToLgint(12304560);


(*1.c*)
fun change(l)=
if null(l) then [1]
else if hd(l)+1<10 then (hd(l)+1)::tl(l)
else  [(hd(l)+1) mod 10]@change(tl(l));

fun addLgint(l1,l2)=
if null(l1) andalso null(l2) then []
else if null(l1) then l2
else if null(l2) then l1
else 
  if hd(l1)+hd(l2)<10 then hd(l1)+hd(l2)::addLgint(tl(l1),tl(l2))
  else (hd(l1)+hd(l2)) mod 10 ::addLgint(tl(l1),change(tl(l2)));
addLgint([9,9,9,0,0,0],[9,9,9,9,9,9]);


(*1.d*)
fun reverse(l)=
if null(l) then []
else reverse(tl(l))@[hd(l)];

fun LgLesseq(l1,l2)=
if null(l1) andalso null(l2) then "True"
else if length(l1)<length(l2) then "True"
else if length(l1)>length(l2) then "False"
else
  if hd(reverse(l1))<=hd(reverse(l2)) then LgLesseq(tl(l1),tl(l2))
  else "False";
LgLesseq([5,2,0],[3,2,1]);


(*Bonus*)
fun addZero(n,c,lFinal)=
if c=n then lFinal
else addZero(n,c+1,[0]@lFinal);

fun multiply(l,n,c,lProduct)=
if c=n then lProduct
else multiply(l,n,c+1,addLgint(l,lProduct));

fun multiplyLgint(l1,l2)=
if l1=[0] orelse l2=[0] then [0]
else
  let
    val length1=length(l2);
    fun product(l)=multiply(l1,hd(l),0,[]);
    fun mult(la,lb,n)=if null(lb)then []
  else addLgint(addZero(length1-n,0,product(lb)),mult(la,tl(lb),n-1));
  in
    mult(l1,l2,length1)
  end;
multiplyLgint([1,9,4,5],[9,9,9,9,7]);


(*2*)
fun sum(a,b)=a+b;

fun sum1(l,n)=
if n=1 then foldl sum 0 (map (fn(p,q,r,s,t)=>p) l)
else if n=2 then foldl sum 0 (map (fn(p,q,r,s,t)=>q) l)
else if n=3 then foldl sum 0 (map (fn(p,q,r,s,t)=>r) l)
else if n=4 then foldl sum 0 (map (fn(p,q,r,s,t)=>s) l)
else foldl sum 0 (map (fn(p,q,r,s,t)=>t) l);

fun hike(l,per,n)=
let
  val average=sum1(l,n) div length(l);
in
  if (per)*100>=110*(average) then per*10 div average-10
  else 0
end;

fun totalHike(l1,l2)=
let
  val (p,q,r,s,t)=hd(l2);
in
  (hike(l1,p,1)+hike(l1,q,2)+hike(l1,r,3)+hike(l1,s,4))*t div 100+t
end;

fun qPerformance(l)=
let
    fun sal(l1,l2)=
  if null(l2) then []
  else totalHike(l1,l2)::sal(l1,tl(l2));
in
  sal(l,l)
end;
qPerformance( [(10, 20, 30, 40, 100000), (30, 30, 20, 50, 150000), (60, 10, 10, 50,200000)]);

fun budgetRaise(l)=
let
    val performance=qPerformance(l);
    val salPrev=sum1(l,5);
    val salNow=foldl sum 0 performance;
in
    real(salNow)/real(salPrev)-1.0
end;
budgetRaise( [(10, 20, 30, 40, 100000), (30, 30, 20, 50, 150000), (60, 10, 10, 50,200000)]);



(*3*)
fun removeTerm(l,x)=
let
  fun remove(l,i,final)=
    if i=x then final@tl(l)
  else remove(tl(l),i+1,final@[hd(l)]);
in
  remove(l,1,[])
end;

fun getTerm(l,i)=
let
  fun term(x::xs,i,c)=
    if i=c then x
    else term(xs,i,c+1);
in
 term(l,i,1)
end;

fun addTerm(l,[x])=
if null(l) then []
else ([x]@hd(l))::addTerm(tl(l),[x]);

fun permutations(l)=
if length(l)=1 then [l]
else if length(l)=2 then [l]@[tl(l)@[hd(l)]]
else
let
  val c=length(l);
  fun perm(l,i)=addTerm(permutations(removeTerm(l,i)),[getTerm(l,i)]);
  fun iter(l,i,res)=if i>c then res
  else iter(l,i+1,res@perm(l,i))
in
  iter(l,1,[])
end;

fun insert(n,[])=n::[]
  |insert(n,x::xs)=if n < x then n::x::xs
else x::insert(n,xs);

fun insort([])=[]
  |insort(x::xs)=insert(x,insort(xs));

fun lexicographicPerm(l)=permutations(insort(l));

print(lexicographicPerm([1,2,3,4]));


(*Bonus*)
fun dup(l,t)=
  if null(l) then []
  else if hd(l)=t then dup(tl(l),t)
  else [hd(l)]@dup(tl(l),t);

fun removeDuplicates(l)=
if null(l) then []
else [hd(l)]@dup(removeDuplicates(tl(l)),hd(l));

fun lexicographicPermDup(l)=
removeDuplicates(lexicographicPerm(l));
print(lexicographicPermDup([1,2,2,3,3]));
