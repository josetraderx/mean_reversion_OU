import numpy as np
from scipy.optimize import minimize

def ou_log_likelihood(params, X, dt):
    mu, theta, sigma = params
    # Asegurar que X es un array 1D limpio
    X = np.array(X).flatten()
    X = X[~np.isnan(X)]
    
    # Calcular diferencias y medias
    X_diff = np.diff(X)
    X_mean = (X[:-1] + X[1:]) / 2
    
    # Calcular log-likelihood
    n = len(X_diff)
    const_term = -0.5 * n * np.log(2 * np.pi * sigma**2 * dt)
    quad_term = -np.sum((X_diff - theta * (mu - X_mean) * dt)**2) / (2 * sigma**2 * dt)
    ll = const_term + quad_term
    return -ll

def estimate_ou_params(series):
    import pandas as pd
    # Convertir DataFrame a Serie si es necesario
    if isinstance(series, pd.DataFrame):
        series = series.iloc[:, 0]
    
    # Convertir a array 1D y limpiar NaNs
    X = np.array(series).flatten()
    X = X[~np.isnan(X)]
    
    # Verificar que hay suficientes datos
    if len(X) < 3:
        raise ValueError("Input series must have at least 3 data points after cleaning.")
    
    # Estimar parámetros
    dt = 1
    initial_params = [np.mean(X), 0.1, np.std(X)]
    result = minimize(ou_log_likelihood, initial_params, args=(X, dt), 
                     bounds=[(None, None), (1e-5, None), (1e-5, None)])
    mu_est, theta_est, sigma_est = result.x
    return mu_est, theta_est, sigma_est
