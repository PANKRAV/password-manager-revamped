"""
A script used for debugging to create three(3) dummy files in :
- data/encryption_data
- data/password_data
- data/user_data
"""
import sys
sys.path.insert(0, 'C:\\Users\\USERPC\\Desktop\\python\\ey\\double_deluxe\\src\\modules')
from pathlib import Path
from helpers.scriptsutil import Dir_Reset
import os
from dotenv import load_dotenv
import json

load_dotenv()
debug = os.getenv("DEBUG")


_json = {
    "enc_json" :{
        "publicKey": "sc\u0000\u0002\u00fe@<\u00f0\u0082_}\u00d8\u001f:\u00f0\u00f7\u00a6 \u00e9\u00c0\u0091\u00fe\u0098d\u00b0[\u00aa\u009d\u00b0G1\u0016\u0003]9y'#wt\n\u0093\u0014\u009e\u00bd\u00fe\u00c9\u00c5:zq\bj\u00c0\u000b\u00c8\u00ac\u0007\u00fa\u00c2\u00fbP\tN\u0099\u00d8p\r\u0013\u00f1*\u0015\u00b6\u0011\u00cf\u00f5R\u0002I<\u0006\u00c0K\u00a4\u00c4\u00d3\u00c7\u00d5\u0012\u00af3\u009f+\u008bI\u0090O\u0018\u00e2\u0082\u0011\u0003L,\u00db9U\bM\u00e1\u00a5\u00cc\u00b2&\u0088\u0003\u009e\u00be\u0099\u00b4\r/29\u00c6\u0085\u0086\u00b8\u00a9#\u001d\u00fe\u00ffm\u0099\u00c0\u00be;w\u00de7\"\u00fa\u00e5\u00b5X\u0087iL_E\u001cz\u00dd\u00ea\u0091\u0081Km\u0080ixB\u00d8\u00fcL<]\u001d\u00ab\u00cc3g[x\u001a|V\u00a2n2\u0084l5\n\u0017\u00d0\u0094\u009fe}\u001c\u0007\u00ef\u00f0\u00aeP\u00cb4\u0085X\u0090\u0017`\u008b\u00d0Q\u0012I(_2\u00c2+x_\u00b3\u0007c\u0098pWj\u001e\u000f\u009c\u001cm\u0018\u00fd\u00ed:\u0091\u00c9A\u0084\u009e\u00aa^/\u00b0\u00e5(\u001eN\u00a74\u00d7\u00bd\u00f9!\u00f1\u0084\u0004gx3\r\u00fb\u009c>i\u0015[Q\u008fk\u00ce\u0012f+U|\u00ee\u0005\f\u00ee\u0006\u00bf\u008b\u00d8\u00c2q\u00c5\"w'\u0094\u00ebP\u00a0U;!q\u00ee\\\u00ca\u00ec\u00cd\u0090\u00bc8\u00ca\u0015\u00ee\u00b8\u00f4\u009c\u00e5\u009d\u007f\u00bbc\u00f4}\u00feii",
        "privateKey": "sc\u0000\u0002\u008et\u0094\r6GwJ\u0005\u0004O\u00dfa\u00b7k(W\u00ab\u00c3\u00ea\u00a1\u00f9\u00fb\u00f3\u0002\u0000\u0012\u009d\u00f2!A\u00e6c\"\u0095\u00ccbLnca\u00b4\u0001\u0004\u0084\u000f\u0013\u00e5\u00c8\u00d0\u009a9\u00f6\u00f9\u00b7\u008e\u001f\u001ev\u0091\n\u008f\u00d8\u001da\u00e0/\u00fc.\u001a\u00b1Y\u00aaz\u00c3\u00bc\u0082c\u000e\u00027\u00cf\u00e3\u001d@J\u00f6\u0016\u00986r\u00d7\u0090\u000f/\u00ca\u008e\u00c7\u00a6\u0099\u00ceOr\u0099>R\u0096\u00de\u00b8C\u00a7\u001c\u009a\u0080\u0019\u00c7`\u00d4\u0010H\u0010\u0089\u00c4\u00b4\n\u00d8@\u00d6bB\u00cbz\u00eaX\u0092\u0007%j\u00f8\"\u00c9\u00b8\\~\u000f\u000ba8\u009a\u00c9x\b\u0016\u00c7\u0010\u00d4\u00f6\u0092(\u000e\u00c3/\u00bc\u0016\u0096\u00ed@\u00bd\u00dd\b\u0098\u0006\u00b33\u00d0\u00c4\u00ae\u0016y\u00c6\u00da\u0003c$\u00bd]O93?zy\u00c9\u001a\u00a1\u0001\u0000\u0003\u001eJ\u0000x\u00c7\u00f4\u00dc\u0019\u0003\u00e3\u0082\u0014/\u00d2\r\u00d4b \\\u00d9\u00ddGQ\u0093\u00ed\u00d1\u0096\u00c8\u00caf\u00f6Fi\u00d1\u0082\u0019\u0003)\u00e9\u00b1%P\u0011\r\u0017\u00e7\u00dd\u00e6\u00fbCv\u000bU\u007f\u000b;V\u000e\u009e\u00c3R\u0089\u0084\u00e2m\u00dcQ\u0010\u00d3\u00c9\"@\u00b9\u0019j\b1\u00a8\u00cf5Z\u001c\u0080\u00ce\u00b0f\u0081\u0097\u00a7\u00e2|i\u0095\u00be!\u0010\u008b\u00be;k\u0013\u0005=\u00a8b! \u00ff\u009f\u00f0\u000e\u00ac\u008f\u00c1'\u00ba[0\u00ca\u00a4\u0002o\u00b0 \u000b\u00dc\u00f5\u00c2\u00da6\u001f\u00b7\t\u001b`\u0097\u00f5\u00b1r\u00bf\u0083\u001f\u0018\u000f\u0097\u00cbIIT\u0088\u00a4D<?\u0019\u00a0\u00ca\u0082b\u00e3\u00e6F\u00ca\u00c3\u00d9\u00e5\u00a5\u009b\u00e8bT#\u00c3\u001ap\u00cf\u0080r\u00aa\u0000+\u009b.h\u001a;\u00ed[st\u0007\u0090\u001c\u0090\u0007\u00be\u00acV\u00fd\u00ea\u00c2\u0083\u00b3\u00d1\u00ae\u00c0\u0010\u00ebv\u00b7\u00aa\u0083N\u008b\u00da\u00ea\u00a0\u00cb\u009c\u0080*\u00e6iZ\u00cb\u00a9\u00d3\u0080\u00a9\u00ff\u00b7\u0093\u0007\u00caR\u00a3\u0001\u0001y\u0086\u00f7\u00eae\u00fd\u0007\u00ac\u009b\u0088\u00d9\u009e\u00d2_\u008f\u0092\u00e4\u00b1`\u007f\u00c7$\u00e3\u008dL\u00a9{y\u00ae\u00d8\u00fa\u00afDR\n\t[\u0096\u00e7\u00c9\u00a0\u0094\u001c\u00dfQ\u0088Y\u00f6j\u000edI\u00f7\u00983+\u00b5\u00ce\u00e1\u00a5\u00e4#\u00a2\u00e8\u00db[E\u00d5e\u00d0@\u00b2\u00e8\u00cb>\u0093I\u00e1\u0001\u0090I]\u001dn\u00f0\u00c0\u0089\u00f9r2\u00d0\u00e8\u00a5\u0096\u0085\u00f6X\u009bhX\u00a8\u009f\u00a0\u00fb\u00c7%_\u0094pH\u00fa,\u009c\u00d2\u009d\u0083xI\u0096!\\\u00f9\u00ae\u0001\n\u00d8}w\u000f\u0096\u00a7b\u008e\u000e\u00fa\u001e$R\u0080;\u00d6\u00a7\u00fd \r\u009c\u0019/{o\u008bc\u009f?\u00ecu\u00daW{\u0019=\u00b5\u00b3\u000b\u00f1\u00ac\u0006\u00e0*\u00c0W>\"nc\u00a9\u00fd\u00bd^/r\u000e9\u0000\u0015xu\u0010e,\u00b1\u0096\u00a1\u007f\u00d1\u00be\u0001\u0019\u0084\u00d0\u00a9?\u0013\u00df\u0090>`\u00f6\u00c1\u00e0\",\u00bf\u00cdT\u00f6\u00f5\u00a9\u00d0d\u000e\u009cT\u00a6\u00fdO\u00d1\u009a\u00c3\u00ee\u00f5\u00bd\u0091J-A\u008d\u0081s\n/P\f\u0083\u008a\u00dd\u00df\u00fbw\u00ee'\u00ea\u008a\u00bb\u00d7\u009a\u00a8\u00f3\u009f\b\u001c\u00db\u008d\u00d4\u00a5\u0098\u00c2o\u00e3\u00eeG6\u00b8t^\u0002\u0084\u0010\u0092\u00a8\u00e7\u00a3\u00de]\u00d2\u0089A\u0003\u00e5\u00c4G\u00bf\u0018l=b\u00c9\u007f$\u00b7\u0007\u009e \u00a3d\u00ecrB\u0097\u00a3\u00c5`\u00c2\u00d7\b\u0098\u009dT\u000e\u00c9\u00b3yE%\u0088\u001e4\u00f0\u0088}<q\u0002\u0084sk\u00dcX\u00ca\u0010\u0092\u00fb\f'x`\nB\u00e2e\u00d0\u00ff\u00f4\u00be\u00f9c\b\u00b0o\u0081\u0091B\u00cd\u00b6\u00c8\u0084\u00abQ\u0015\u00f4\u00dc\u00b4*\u00e2\u009d\u00fah!\u00c5 5\u0001\u00aak)\u00d3\u0003=\u0018\u00e4\u00e2p\u00c1\u00d0\u00171\u00ba\u00eaH\u001bKF3.I\u00df\u0002\u001f\u00ec\u00a1\u00cfS\u0083\u00f7\u0005\u00a13#\u00b0--\u00e1iR\u00e5b\tG\u00f2'|i\u0080\u0096\u00e6zN\u00d0\u0097\u0095\u00cc\u00b4s\u001e\u00c0\u00b3mp]:(\u0081\u00f7\u008eT;Z2\u00c3V6\u00da&fr\u0090U\u0006R\u00bf\u008fX8\u00c6\u00f2\u00fc\u009a\u0086\u00a2\u0099vX\f$\u00aa}Y\\7\u00f9\u0011J\u00ce4\u00f6^\u00df\u00e4\u00c0\u00ce\u0018F\u00ef;#\u00f6tr\u00b2\u00e1N\u00ad\u0016\u0094\u00f2\u00b3,D\u0097\u0080\u0097/|",
        "security": 1024
    },
    "pwd_json" : {
        "foo": {
            "username": "norm",
            "pwd": "A\u008fZ8\u00a5\u00de\u0082$\u008b\u0013\u00da\u00ec\u0080\u00adF\u0093\u00bf\u00c9eg\u00e3\u008b\u00ee\u00a1\u00e1\u001b3\u0004\u007f\u00e8>\u00ee\u00ce\u00cf|A\u008b\u001b\u00ed+l\u008b\u00e1\u00b9\u0001\u00c6\u00f2:3:\u0088.\u00fe;\u00f8\u00a3\u00f2E\u0080#\u00d96\u0092=\u00e5\u001c\u0011\u00a3\u008be\u00f3\u00c1\u0003\u00baLny\u001b\u00cf\u00d0\u00db1\u00a6\u0017\u00c3\u001bM\u00e8\u001b!\u00ea20\u00d42&\u00f1\u00dc-e\u00aa\u0002/\u00a2\u0093X\u00ec\"\u00a0\u001a,\u00bbu\u000b\u001d54\u00ff=*\u00f4\u00ea\u00b7\u00c5Kh\u00bd\u008b",
            #Right
            "email": "email"
        },
        "here": {
            "username": "egw",
            "pwd": "\b\u00ff\u00b0/O\u009d\u00de\u00cb\u00dd\u0000\u00f8\u0006\u0011Q.\u00f9z:NZ0\u00ab\u0086`\u00978L\u008a$\u00c6\u00cc\troK\u0011,C\u00f3\u00de\u0005\u00b3\u00de\u00e9i\u00e4g\u001b\u00b5\u00acJl.5E\u00ed\u00e76Xf\u001e\u00b7\u00eb\u0080(\u0095bu\u00cd^\u00f5\u0013\u008b\u009b\u00d2t\u00ce+U\u00ff\u0080cY\u009c\u00c8\u00c1@\u00fc\u0017\u00dd\u00e4\u00cf#?\"\u0093\u00fb+\b\u0096\u009dL\u00f6a\u00a7\u0018\u00b1\u00e2\u00d4>N3\u00a9\u00bd\u00cbsJ\u009c`\u00d0\u00b8\u00b5\u00c0\u00fd\u00a3\u0088K-",
            #4Cr)l^0@8)4p9E1OQ6Q@
            "email": "gmail"
        }
    },
    "user_json" : {
    "name": "egw",
    "key": "39c24f75616011eca4d99fa9fe4cdd32f82107c4d9f4a2797daec7f77e52cd6cffa3c2bad2ee8e3f45ae76c993eac6e846fd7966e9d80d7c4bc317ef20dbe851",
    #user_key : a
    "salt": "52z54"
    }
}


def main():
    abspath = Path(os.path.abspath(__file__))
    os.chdir(abspath.parent.parent.parent)

    if debug == "1":
        with Dir_Reset.from_string("data/encryption_data") as cur :
            if "dummy.json" in cur.dirs :
                print("Overwriting previous data/encryption_data json file")
            with Path("dummy.json").open("wt") as w_f :
                w_f.write(json.dumps(_json["enc_json"], indent=4))

        with Dir_Reset.from_string("data/password_data") as cur :
            if "dummy.json" in cur.dirs :
                print("Overwriting previous data/password_data json file")
            with Path("dummy.json").open("wt") as w_f :
                w_f.write(json.dumps(_json["pwd_json"], indent=4))

        with Dir_Reset.from_string("data/user_data") as cur :
            if "dummy.json" in cur.dirs :
                print("Overwriting previous data/user_data json file")
            with Path("dummy.json").open("wt") as w_f :
                w_f.write(json.dumps(_json["user_json"], indent=4))



    elif debug == "0" :
        print("debug setting is turned off")

    else :
        print("bad .env configuration")


if __name__ == "__main__" :
    main()