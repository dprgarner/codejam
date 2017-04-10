-- 2015, Qualification round, A
-- https://code.google.com/codejam/contest/6224486/dashboard
--

module Main where

import Data.Char (digitToInt)
import Data.List (inits)

import Codejam (solve)

type Case = [Int]


getCases :: [String] -> [Case]
getCases = (map $ map digitToInt . last . words) . tail

solveCase :: Case -> String
solveCase case_ =
  let
    partialSums = map sum $ tail $ inits case_
    values = map (\(x, y) -> x - y) $ zip [1..] partialSums
  in 
    show $ foldr max 0 values

main :: IO ()
main = solve getCases solveCase
