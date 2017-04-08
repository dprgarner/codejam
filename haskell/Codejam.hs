module Codejam where

import Data.List (lines)

solveFromString :: ([String] -> [a]) -> (a -> String) -> String -> String
solveFromString getCases solveCase input =
  let cases = (getCases.lines) input
      solutions = map solveCase cases
      formatCase (i, s) = "Case #" ++ show i ++ ": " ++ s
      formattedSolutions = map formatCase $ zip [1..] solutions
  in
    unlines formattedSolutions

solve :: ([String] -> [a]) -> (a -> String) -> IO ()
solve getCases solveCase =
  putStr.solveFromString getCases solveCase =<< getContents