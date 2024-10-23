from Crypto.Util.number import getPrime
from math import prod
from sympy import nextprime
from random import choices

with open('flag.txt', 'rb') as fs:
    flag = fs.read().strip()

primes = [getPrime(512) for _ in range(9)]
print(f"{prod(primes) = }")
print(f"{prod(p - 1 for p in primes) = }")

primes2 = [nextprime(p) for p in choices(primes, k=3)]
n = prod(primes2)
e = 65537
c = pow(int.from_bytes(flag, 'big'), e, n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')

# 363364907814244019888662301376841344262476227242899756862391470731421569394957444030214887114615748277199649349781524749919652160244484352285668794188836866602305788131186220057989320357344904731322223310531945208433910803617954798258382169132907508787682006064930747033681966462568715421005454243255297306718356766130469885581576362173340673516476386201173298433892314145854649884922769732583885904512624543994675379894718657682146178638074984373206937523380103438050549181568015985546172618830480078894445808092527561363650503540062128543705172678754195578429520889784813733491180748361345720247750720179608752244490362713103319685024237941527268458213442611663415417005556439749055222361212059968254748751273361732365487788593341859760309778894350385339764442343374673786357175846291309425081492959910254127778240522152676060766139057453197528944251599979227271074508795482632471242983094008619339488744362509349734218480932255216087706001484182136783834973304870508270118505737767002256270427907341952256516206663258530300791364944105025764611810001781971638030661367630116818647252727909489405550104641122269772492252464714694507693447974171377200402508765841829763548525530878309985480248379655169722567051495205792089930014228403456098065971372039443284193603395249634283366194562380309469628114581468645669390610963076340643757972439104287127375438663839421605531570285615180251
# 363364907814244019888662301376841344262476227242899756862391470731421569394957444030214887114615748277199649349781524749919652160244484352285668794188836492373364350673588273863828369502073826782362255108313852264064760467561392054178047091483873483255491431451728274259516789065331176728192953741805933100379191778599394515981288225535175013258094287912195847642598436035132783919453991516358280321085873745330313812205910011387125778714795906023110368957596998222544234082487264006696812862179916726781327290284827659294751262185328816323311831349296593013038823107653943652771448719760448938995150646738377177532550757319539185878535087009904848382493668686831331474113789651777885239747000076063679062106375348803749466079052774597412239427050432901553466002731972993029311850718200685157193170716432600165476733200831046297530470544781309612128231925681374239849452623513538498417735984094919756374577623486416462101457492789215144166273775249387638107644634704270216130852885082174564648445147377239033930079759024399532146184753110240154062693457622208373371290126810856885343328090305620627668495081760346853701632815149478447405718664667978825807101325764916405446176183238866136433205933785973568759281210319422288153910340542098573782006262190181726245838857185687242960093445000287347616796984610291664809895901301187179157382169999966124177588884152267266994164841066291200
# n = 899081756851564072995842371038848265712822308942406479625157544735473115850983700580364485532298999127834142923262920189902691972009898741820291331257478170998867183390650298055916005944577877856728843264502218692432679062445730259562784479410120575777748292393321588239071577384218317338474855507210816917917699500763270490789679076190405915250953860114858086078092945282693720016414837231157788381144668395364877545151382171251673050910143023561541226464220441
# e = 65537
# c = 841335863342518623856757469220437045493934999201203757845757404101093751603513457430254875658199946020695655428637035628085973393246970440054477600379027466651143466332405520374224855994531411584946074861018245519106776529260649700756908093025092104292223745612991818151040610497258923925952531383407297026038305824754456660932812929344928080812670596607694776017112795053283695891798940700646874515366341575417161087304105309794441077774052357656529143940010140