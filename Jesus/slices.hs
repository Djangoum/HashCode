main :: IO ()
main = do
    putStrLn "Hello world!"
    -- prod = 2 * 3
    -- putStrLn prod

-- sliceTypes' = [ (a,b) | a <- [1..6], b <- [1..6], a * b <= 6, a * b >= 2 ]
-- sliceTypes'
-- [ (a,b) | a <- [1..h], b <- [1..h], a * b <= h, a * b >= 2 * l ]