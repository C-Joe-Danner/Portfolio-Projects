--Covid 19 Data Exploration 
--Skills used: Joins, CTE's, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data Types

--Selecting starting data

SELECT location, date, total_cases, new_cases, total_deaths, population
FROM [Portfolio Project 1]..CovidDeaths
ORDER BY 1,2;

--  Total Cases vs Total Deaths

SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100  as DeathPercentage
FROM [Portfolio Project 1]..CovidDeaths
WHERE location like '%states%'
AND continent is not NULL
ORDER BY date DESC;

--  Total Cases vs Population

SELECT location, date, total_cases, population, (total_cases/population)*100  as PercentPopulationInfected
FROM [Portfolio Project 1]..CovidDeaths
WHERE location = 'Hong Kong'
AND continent is not NULL
ORDER BY date DESC;

--  Highest Infection Rate compared to Population

SELECT location, population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population))*100 as HighPercentInfected
FROM [Portfolio Project 1]..CovidDeaths
GROUP BY location, population
ORDER BY HighPercentInfected DESC;

--  Highest Death Count by Contry

SELECT location, MAX(cast(total_deaths as int)) as TotalDeathCount
FROM [Portfolio Project 1]..CovidDeaths
WHERE continent is not NULL
GROUP BY location
ORDER BY TotalDeathCount DESC;

--  Highest Death Count by Continent

SELECT continent, MAX(cast(total_deaths as int)) as DeathCountByContinent
FROM [Portfolio Project 1]..CovidDeaths
WHERE continent is not NULL
GROUP BY continent
ORDER BY DeathCountByContinent DESC;

--  Global Numbers

SELECT date, SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
FROM [Portfolio Project 1]..CovidDeaths
WHERE continent is not NULL and total_cases is not NULL
GROUP BY date
ORDER BY date ASC

--  Total Population vs Vaccinations

--Rolling Count
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) as RollingCount
FROM [Portfolio Project 1]..CovidDeaths dea
JOIN [Portfolio Project 1]..CovidVaccintions vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not NULL
ORDER BY 2,3;

--  Can use CTE or Temp Table to perfrom calculations on Partition By in previous query

--CTE version
WITH PopVac (continent, location, date, population, new_vaccinations, RollingCount)
as
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) as RollingCount
FROM [Portfolio Project 1]..CovidDeaths dea
JOIN [Portfolio Project 1]..CovidVaccintions vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not NULL
)
SELECT *, (RollingCount/population)*100 as RollingPercent
FROM PopVac

--Temp Table version

DROP TABLE if exists #PercentPopVac
CREATE TABLE #PercentPopVac
(continent nvarchar(255), loaction nvarchar(255), date datetime, population numeric, new_vaccinations numeric, RollingCount numeric)

INSERT INTO #PercentPopVac
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) as RollingCount
FROM [Portfolio Project 1]..CovidDeaths dea
JOIN [Portfolio Project 1]..CovidVaccintions vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not NULL

SELECT *, (RollingCount/population)*100 as RollingPercent
FROM #PercentPopVac
ORDER BY 2,3

--  Creating View to store data for future visualizations

CREATE VIEW RollingCount as
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) as RollingCount
FROM [Portfolio Project 1]..CovidDeaths dea
JOIN [Portfolio Project 1]..CovidVaccintions vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not NULL;

