import Control.Monad.State

eval src = evalState pn $ words src

op f = do
    x <- pn
    y <- pn
    return $ f x y

pn = do
    (x:xs) <- get
    put xs
    case x of
        "+" -> op (+)
        "*" -> op (*)
        _   -> return $ read x

main = do
    print $ eval "+ 1 2"
    print $ eval "* 1 2"
    print $ eval "1"
    print $ eval "+ 2 * 3 4"
    print $ eval "+ * 2 3 4"