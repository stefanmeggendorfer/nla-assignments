// Compile with C++17:
// g++ -std=c++17 -o steepest-decent steepest-decent.cc

#include "laplace.h"

int main()
{
  const unsigned int d = 2;
  const unsigned int n = 20;

  if (n==0) assert(false);

  Laplace<d> A(n);
  if (n<8){
    A.print();
    A.print_sparsity();
  }

  const unsigned int n_dofs = A.size();

  const std::vector<double> b(n_dofs, 1.);
  std::vector<double> x(n_dofs, 0.);

  const unsigned int tol = 1.e-14;
  const unsigned int n_steps = 50;
  steepest_decent(A, b, x, tol, n_steps);
}
