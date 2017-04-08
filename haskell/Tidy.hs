-- Qualification Round, 2017
-- https://code.google.com/codejam/contest/3264486/dashboard#s=p1
-- 

module Main where

import Data.Char (digitToInt, intToDigit)
import Data.List (inits)

import Codejam (solve)

type Case = [Int]

getCases :: [String] -> [Case]
getCases = (map $ map digitToInt) . tail

isTidy :: Case -> Bool
isTidy case_ = all (\(x, y) -> x <= y) $ zip case_ $ tail case_

getFirstTidyPart :: [Int] -> Case
getFirstTidyPart xs = 
  last $ takeWhile isTidy $ inits xs

decrementLastDigit :: [Int] -> [Int]
decrementLastDigit xs = init xs ++ [(last xs) - 1]

appendNines :: Int -> [Int] -> Case
appendNines n xs =
  xs ++ (take n $ repeat 9)

goBackBeforeUntidyPart :: Case -> Case
goBackBeforeUntidyPart case_ =
  let
    tidyPart = getFirstTidyPart case_
  in
    appendNines (length case_ - length tidyPart) $ decrementLastDigit tidyPart

iterativelyFindLastTidyNumber :: Case -> Case
iterativelyFindLastTidyNumber case_ =
  if
    isTidy case_
  then
    case_
  else
    iterativelyFindLastTidyNumber $ goBackBeforeUntidyPart case_

solveCase :: Case -> String
solveCase case_ =
  map intToDigit $ dropWhile (==0) $ iterativelyFindLastTidyNumber case_

main :: IO ()
main = solve getCases solveCase