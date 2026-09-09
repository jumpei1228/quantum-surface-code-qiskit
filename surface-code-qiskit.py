"""
表面符号(サーフェスコード)をQiskitで実装｜XとZを同時に見張る2次元誤り訂正

元記事: https://quantum.yurufuwa.work/learn/surface-code-qiskit
ゆるふわ量子コンピュータ (quantum.yurufuwa.work) の解説記事から抜粋したコードです。
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def z_stabilizer(error_qubit=None):
    qc = QuantumCircuit(5, 1)   # q0-q3: データ（正方形の四隅）, q4: アンシラ
    if error_qubit is not None:
        qc.x(error_qubit)       # データにビットフリップ(X)エラーを注入
    for q in range(4):
        qc.cx(q, 4)             # 各データをアンシラへCNOT → パリティを転写
    qc.measure(4, 0)
    return qc

sim = AerSimulator()
for label, eq in [("エラー無し", None), ("q0にXエラー", 0), ("q2にXエラー", 2)]:
    counts = sim.run(z_stabilizer(eq), shots=1000).result().get_counts()
    print(label, ":", counts)

def x_stabilizer(error_qubit=None):
    qc = QuantumCircuit(5, 1)
    for q in range(4):
        qc.h(q)                   # データを |++++> に（XXXXの固有状態にそろえる）
    qc.h(4)                      # アンシラを |+> に
    if error_qubit is not None:
        qc.z(error_qubit)        # データに位相フリップ(Z)エラーを注入
    for q in range(4):
        qc.cx(4, q)               # アンシラ制御でデータへCNOT
    qc.h(4)                      # 基底を戻してX測定と等価に
    qc.measure(4, 0)
    return qc

for label, eq in [("エラー無し", None), ("q1にZエラー", 1), ("q3にZエラー", 3)]:
    counts = sim.run(x_stabilizer(eq), shots=1000).result().get_counts()
    print(label, ":", counts)

def prepare_code_state(qc):
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.cx(0, 3)          # データを (|0000>+|1111>)/√2 に

def surface_patch(error_gate=None, error_qubit=None):
    qc = QuantumCircuit(6, 2)     # q0-q3: データ, q4: Zスタビライザー用, q5: Xスタビライザー用
    prepare_code_state(qc)
    qc.h(5)

    if error_gate == "x":
        qc.x(error_qubit)
    if error_gate == "z":
        qc.z(error_qubit)

    for q in range(4):
        qc.cx(q, 4)               # Zスタビライザー（ZZZZ）→ Xエラーを検出
    for q in range(4):
        qc.cx(5, q)               # Xスタビライザー（XXXX）→ Zエラーを検出
    qc.h(5)

    qc.measure(4, 0)
    qc.measure(5, 1)
    return qc

for label, gate, eq in [
    ("エラー無し", None, None),
    ("Xエラー(q0)", "x", 0),
    ("Zエラー(q0)", "z", 0),
]:
    counts = sim.run(surface_patch(gate, eq), shots=1000).result().get_counts()
    print(f"{label:12s}:", counts)
