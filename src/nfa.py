# src/nfa.py

class NFA:
    def __init__(self, states, alphabet, start_state, final_states, transitions):
        """
        Inisialisasi komponen Formal NFA (5-tuple)
        """
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.start_state = start_state
        self.final_states = set(final_states)
        # Format transisi: {("q0", "0"): {"q0", "q1"}}
        self.transitions = transitions

    def process_string(self, input_string, verbose=True):
        """
        Memproses string input dan menampilkan langkah eksekusinya.
        Mengembalikan tuple: (is_accepted, logs)
        """
        current_states = {self.start_state}
        logs = []

        if verbose:
            print("\n----------------------------------")
            print(f"Proses Pembacaan String: '{input_string}'")
            print(f"State Awal: {current_states}")
            print("----------------------------------")

        for symbol in input_string:
            if symbol not in self.alphabet:
                msg = f"Error: Simbol '{symbol}' tidak ada dalam alfabet {self.alphabet}!"
                logs.append(msg)
                if verbose:
                    print(msg)
                return False, logs

            next_states = set()
            for state in current_states:
                # Mengambil himpunan state tujuan dari tabel transisi
                next_states.update(self.transitions.get((state, symbol), set()))

            current_states = next_states
            msg = f"Membaca simbol '{symbol}' -> State aktif: {current_states}"
            logs.append(msg)
            if verbose:
                print(msg)

        # Evaluasi apakah ada final state yang aktif di akhir string
        is_accepted = bool(current_states.intersection(self.final_states))
        
        if verbose:
            if is_accepted:
                print(f"\nHasil Akhir: STRING DITERIMA (State akhir {current_states.intersection(self.final_states)} aktif)")
            else:
                print("\nHasil Akhir: STRING DITOLAK (Tidak menyentuh state akhir)")

        return is_accepted, logs