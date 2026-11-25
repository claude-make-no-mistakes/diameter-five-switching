import Init

namespace Switching

/-! The counting step of the one-branch switching construction. -/

theorem four_choices (a : Nat) (enough : 5 ≤ a) (u v w : Nat) :
    ∃ k : Nat, 1 ≤ k ∧ k < a ∧ k ≠ u ∧ k ≠ v ∧ k ≠ w := by
  apply Classical.byContradiction
  intro missing
  have only (k : Nat) (positive : 1 ≤ k) (within : k < a) :
      k = u ∨ k = v ∨ k = w := by
    by_cases h₁ : k = u
    · exact Or.inl h₁
    by_cases h₂ : k = v
    · exact Or.inr (Or.inl h₂)
    by_cases h₃ : k = w
    · exact Or.inr (Or.inr h₃)
    exact False.elim (missing ⟨k, positive, within, h₁, h₂, h₃⟩)
  have h₁ := only 1 (by omega) (by omega)
  have h₂ := only 2 (by omega) (by omega)
  have h₃ := only 3 (by omega) (by omega)
  have h₄ := only 4 (by omega) (by omega)
  omega

end Switching

#print axioms Switching.four_choices
