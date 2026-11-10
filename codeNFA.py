
# ==========================================
# PROGRAM SIMULASI NFA
# Mengenali String Biner yang Berakhiran 01
# ==========================================

# Daftar state
states = {"q0", "q1", "q2"}

# Alfabet
alphabet = {"0", "1"}

# State awal
start_state = "q0"

# State akhir
final_states = {"q2"}

# Fungsi transisi NFA
transitions = {
    ("q0", "0"): {"q0", "q1"},
    ("q0", "1"): {"q0"},
    ("q1", "0"): set(),
    ("q1", "1"): {"q2"},
    ("q2", "0"): set(),
    ("q2", "1"): set()
}


# Fungsi untuk menjalankan NFA
def run_nfa(input_string):

    # Memulai dari state awal
    current_states = {start_state}

    print("\nProses Pembacaan String:")
    print("Input:", input_string)
    print("State awal:", current_states)

    # Membaca setiap karakter
    for symbol in input_string:

        if symbol not in alphabet:
            print("Simbol tidak valid:", symbol)
            return False

        next_states = set()

        # Memeriksa seluruh state aktif
        for state in current_states:

            next_states.update(
                transitions.get((state, symbol), set())
            )

        current_states = next_states

        print("Membaca:", symbol)
        print("State aktif:", current_states)

    # Memeriksa apakah ada state akhir yang aktif
    if current_states.intersection(final_states):
        print("\nHasil: STRING DITERIMA")
        return True

    else:
        print("\nHasil: STRING DITOLAK")
        return False


# Program utama
print("===================================")
print("       SIMULASI PROGRAM NFA")
print("===================================")
print("Pola: String biner berakhiran 01")
print("Alfabet: {0, 1}")

while True:

    user_input = input("\nMasukkan string biner: ")

    run_nfa(user_input)

    ulang = input("\nCoba lagi? (y/n): ")

    if ulang.lower() != "y":
        print("\nProgram selesai.")
        break
