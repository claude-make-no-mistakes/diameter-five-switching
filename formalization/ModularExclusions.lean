import Init

namespace Switching

/-- Horner evaluation of coefficients in ascending order. -/
def evalPoly (coeffs : List Int) (x : Int) : Int :=
  coeffs.foldr (fun coefficient rest => coefficient + x * rest) 0

theorem eval_mod (coeffs : List Int) (x m : Int) :
    evalPoly coeffs x % m = evalPoly coeffs (x % m) % m := by
  induction coeffs with
  | nil => rfl
  | cons a coeffs ih =>
    simp only [evalPoly, List.foldr_cons] at ih ⊢
    rw [Int.add_emod, Int.add_emod a ((x % m) * _)]
    congr 1
    congr 1
    rw [Int.mul_emod, Int.mul_emod (x % m), ih, Int.emod_emod]
    simp only [Int.emod_emod]
    simpa only [Int.emod_emod] using
      (Int.mul_emod (x % m) (coeffs.foldr (fun a b => a + x % m * b) 0) m).symm

def nonzeroResidues (modulus : Nat) (coeffs : List Int) : Bool :=
  (List.range modulus).all (fun r => evalPoly coeffs r % modulus != 0)

theorem no_integer_root (modulus : Nat) (coeffs : List Int)
    (positive : 0 < modulus) (certificate : nonzeroResidues modulus coeffs = true)
    (x : Int) : evalPoly coeffs x ≠ 0 := by
  intro hzero
  have hpos : (0 : Int) < modulus := by omega
  have hlow : 0 ≤ x % (modulus : Int) := Int.emod_nonneg x (by omega)
  have hhigh : x % (modulus : Int) < modulus := Int.emod_lt_of_pos x hpos
  let index := (x % (modulus : Int)).toNat
  have mem : index ∈ List.range modulus := List.mem_range.mpr (by omega)
  have residue := List.all_eq_true.mp certificate index mem
  have cast : (index : Int) = x % (modulus : Int) := by omega
  simp only [cast, bne_iff_ne] at residue
  apply residue
  rw [← eval_mod, hzero]
  simp

def reflectedResultants : List (Nat × List Int) := [
  (3, [4, -20, 21, -3, 0, -1]),
  (3, [16, -40, 24, -4, 4, -1]),
  (3, [4, -116, 81, 11, 0, -3]),
  (5, [-72, -72, 100, 6, -7, -2]),
  (3, [-604, -20, 417, -23, -34, -5]),
  (2, [1, 0, -11, 0, -1]),
  (5, [18, -14, -2, -1]),
  (7, [-3, 5, 29, -23, -5, -1]),
  (7, [-16, 28, 38, -38, -8, -1]),
  (17, [-45, 81, 39, -59, -11, -1]),
  (3, [-20, 76, 9, -127, 48, -9]),
  (3, [-8, 64, 48, -154, 21, -9]),
  (3, [4, 52, 123, -235, -6, -9]),
  (3, [-8, 112, 180, -370, -33, -9]),
  (3, [-68, 316, 165, -559, -60, -9]),
  (3, [-11, 55, -39, -57, 48, -4]),
  (3, [-8, 54, -30, -65, 36, -4]),
  (5, [-1, 39, 3, -97, 24, -4]),
  (3, [4, 34, 36, -153, 12, -4]),
  (3, [1, 63, 45, -233, 0, -4]),
  (5, [-76, 460, -547, -299, 520, -25]),
  (5, [-72, 504, -564, -314, 445, -25]),
  (5, [-36, 404, -361, -479, 370, -25]),
  (5, [8, 280, -88, -794, 295, -25]),
  (5, [36, 252, 105, -1259, 220, -25])]

theorem reflected_residues :
    reflectedResultants.all (fun (modulus, coeffs) => nonzeroResidues modulus coeffs) = true := by decide

theorem reflected_exclusions (entry : Nat × List Int)
    (member : entry ∈ reflectedResultants) (parameter : Int) :
    evalPoly entry.2 parameter ≠ 0 := by
  have positivity : reflectedResultants.all (fun p => decide (0 < p.1)) = true := by decide
  exact no_integer_root entry.1 entry.2
    (of_decide_eq_true (List.all_eq_true.mp positivity entry member))
    (List.all_eq_true.mp reflected_residues entry member) parameter

end Switching

#print axioms Switching.no_integer_root
#print axioms Switching.reflected_residues
#print axioms Switching.reflected_exclusions
