#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

class FStudioAnalyticsProviderModule : public IModuleInterface
{
public:
	/** IModuleInterface implementation */
	virtual void StartupModule() override;
};