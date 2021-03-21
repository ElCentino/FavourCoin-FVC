from ecpy.curves import Curve,Point
from ecpy.keys import ECPublicKey, ECPrivateKey
from ecpy.ecdsa import ECDSA

class KeyGenerator:

    def __init__(self) -> None:
    
        cv = Curve.get_curve('secp256k1')

        pu_key = ECPublicKey()
        pv_key = ECPrivateKey()

        print(pu_key)
        print(pv_key)


KeyGenerator()