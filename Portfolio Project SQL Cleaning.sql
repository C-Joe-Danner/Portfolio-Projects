/*
Cleaning Data in SQL Queries

Skills - Standarizing Date Format, Populating Data, Breaking Out Data,
Chaning "Y and N" to "Yes and No", Removing Duplicates, Deleting Unused Columns
*/


SELECT TOP 100 *
FROM [Portfolio Project 1]..NashvilleHousingData;

-- Standardize Date Format --

SELECT SalesDate, CONVERT(Date, SaleDate)
FROM [Portfolio Project 1]..NashvilleHousingData;

ALTER TABLE NashvilleHousingData
ADD SalesDate Date;

UPDATE NashvilleHousingData
SET SalesDate = CONVERT(Date, SaleDate);

-- Populate Property Address data --

SELECT *
FROM [Portfolio Project 1]..NashvilleHousingData
WHERE PropertyAddress is NULL;

SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM [Portfolio Project 1]..NashvilleHousingData a
JOIN [Portfolio Project 1]..NashvilleHousingData b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress is NULL;

UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM [Portfolio Project 1]..NashvilleHousingData a
JOIN [Portfolio Project 1]..NashvilleHousingData b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress is NULL;

-- Breaking out Address into Individual Columns --

SELECT PropertyAddress
FROM [Portfolio Project 1]..NashvilleHousingData;

SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1) as Address,
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1, LEN(PropertyAddress)) as City
FROM [Portfolio Project 1]..NashvilleHousingData;

ALTER TABLE NashvilleHousingData
ADD PropertySplitAddress Nvarchar(255);

UPDATE NashvilleHousingData
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1);

ALTER TABLE NashvilleHousingData
ADD PropertySplitCity Nvarchar(255);

UPDATE NashvilleHousingData
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1, LEN(PropertyAddress));

SELECT PropertySplitAddress, PropertySplitCity 
FROM [Portfolio Project 1]..NashvilleHousingData;

-- Alternate Method --

SELECT OwnerAddress
FROM [Portfolio Project 1]..NashvilleHousingData;

SELECT
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)
,PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)
,PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
FROM [Portfolio Project 1]..NashvilleHousingData;

ALTER TABLE NashvilleHousingData
ADD OwnerSplitAddress Nvarchar(255);

UPDATE NashvilleHousingData
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3);

ALTER TABLE NashvilleHousingData
ADD OwnerSplitCity Nvarchar(255);

UPDATE NashvilleHousingData
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2);

ALTER TABLE NashvilleHousingData
ADD OwnerSplitState Nvarchar(255);

UPDATE NashvilleHousingData
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1);

Select OwnerSplitAddress, OwnerSplitCity, OwnerSplitCity
From [Portfolio Project 1]..NashvilleHousingData;

-- Change Y and N to Yes and No in "Sold as Vacant" field --

SELECT DISTINCT(SoldAsVacant), COUNT(SoldAsVacant)
FROM [Portfolio Project 1]..NashvilleHousingData
GROUP BY SoldAsVacant
ORDER BY 2;

SELECT SoldAsVacant
, CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
		WHEN SoldAsVacant = 'N' THEN 'No'
		ELSE SoldAsVacant
		END
FROM [Portfolio Project 1]..NashvilleHousingData;

UPDATE NashvilleHousingData
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'YES'
		WHEN SoldAsVacant = 'N' THEN 'No'
		ELSE SoldAsVacant
		END;

-- Remove Duplicates --

WITH RowCTE AS(
SELECT *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID, PropertyAddress, SalePrice, SaleDate, LegalReference
	ORDER BY UniqueID) row_num
FROM [Portfolio Project 1]..NashvilleHousingData
)
DELETE
FROM RowCTE
WHERE row_num > 1;

-- Delete Unused Columns --

ALTER TABLE [Portfolio Project 1]..NashvilleHousingData
DROP COLUMN OwnerAddress, PropertyAddress, SaleDate, TaxDistrict;

SELECT *
FROM [Portfolio Project 1]..NashvilleHousingData;

